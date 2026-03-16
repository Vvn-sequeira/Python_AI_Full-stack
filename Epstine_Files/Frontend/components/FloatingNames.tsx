
import React, { useState, useEffect, useCallback, useMemo } from 'react';

/**
 * Returns true if the user is on a mobile or tablet device.
 * Detection uses two signals:
 *  1. Coarse pointer (touch screen)  — covers phones & tablets
 *  2. Screen width ≤ 1024px          — extra safety net
 */
function useIsMobileOrTablet(): boolean {
  const getIsMobile = () =>
    window.matchMedia('(pointer: coarse)').matches ||
    window.matchMedia('(max-width: 1024px)').matches;

  const [isMobile, setIsMobile] = useState<boolean>(getIsMobile);

  useEffect(() => {
    const mq = window.matchMedia('(max-width: 1024px)');
    const handler = () => setIsMobile(getIsMobile());
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, []);

  return isMobile;
}

const RED_NAMES = [
  'Donald Trump', 'Melania Trump', 'Ivanka Trump', 'JD Vance',
  'Bill Clinton', 'Hillary Clinton', 'Barack Obama', 'Michelle Obama',
  'Joe Biden', 'Jill Biden',
];

const OTHER_NAMES = [
  'Howard Lutnick', 'Bill Richardson', 'Steve Bannon', 'Kathryn Ruemmler',
  'Hakeem Jeffries', 'Antony Blinken', 'Marco Rubio', 'Kamala Harris',
  'Larry Summers', 'Chuck Schumer', 'George W. Bush', 'Nikki Haley',
  'Mike Huckabee', 'Mike Pompeo', 'Alexandria Ocasio-Cortez', 'Mike Pence',
  'James Comey', 'Ron DeSantis', 'Robert F. Kennedy Jr.', 'Jeff Bezos',
  'Elon Musk', 'Mark Zuckerberg', 'Jared Kushner', 'Richard Branson',
  'Bill Gates', 'Les Wexner', 'Leon Black', 'Peter Thiel',
  'Sultan bin Sulayem', 'Josh Harris', 'Reid Hoffman',
  "Francisco D'Agostino", 'Anil Ambani', 'Eva Andersson-Dubin',
  'Glenn Dubin', 'Dan Ariely', 'Peter Attia', 'Doug Band',
  'Tom Barrack', 'Casey Wasserman', 'Prince Andrew', 'Sarah Ferguson',
  'Queen Elizabeth II', 'Princess Diana', 'Prince Harry', 'Prince Philip',
  'Peter Mandelson', 'Ehud Barak', 'José María Aznar', 'Sergei Belyakov',
  'Woody Allen', 'David Copperfield', 'Elvis Presley', 'Michael Jackson',
  'Stephen Hawking', 'Jack Horner', 'Richard Axel', 'Joscha Bach',
  'David Gelernter', 'Jean-Luc Brunel', 'Darren Indyke', 'Alan Dershowitz',
  'Ariane de Rothschild', 'Leon Botstein', 'Robert Maxwell',
  'Ghislaine Maxwell', 'Mariette DiChristina', 'Tony Hawk', 'Ana Botella',
  'Jeffrey Epstein',
];

function seededRand(seed: number) {
  const x = Math.sin(seed + 1) * 10000;
  return x - Math.floor(x);
}

interface NameItem {
  name: string;
  isRed: boolean;
  x: number;
  y: number;
  size: number;
  opacity: number;
  duration: number;
  delay: number;
  driftX: number;
  driftY: number;
  depth: number;  // parallax depth factor
  rotation: number;
}

const FloatingNames: React.FC = () => {
  const isMobile = useIsMobileOrTablet();
  const [mouse, setMouse] = useState({ x: 0, y: 0 });

  const handleMouseMove = useCallback((e: MouseEvent) => {
    const cx = window.innerWidth / 2;
    const cy = window.innerHeight / 2;
    setMouse({
      x: (e.clientX - cx) / cx,
      y: (e.clientY - cy) / cy,
    });
  }, []);

  useEffect(() => {
    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, [handleMouseMove]);

  const items = useMemo<NameItem[]>(() => {
    const all = [
      ...RED_NAMES.map(n => ({ name: n, isRed: true })),
      ...OTHER_NAMES.map(n => ({ name: n, isRed: false })),
    ];
    return all.map((item, i) => ({
      ...item,
      x: seededRand(i * 7) * 88,
      y: seededRand(i * 13) * 88,
      size: item.isRed ? 13 + seededRand(i * 3) * 10 : 10 + seededRand(i * 3) * 9,
      opacity: item.isRed
        ? 0.55 + seededRand(i * 5) * 0.25
        : 0.30 + seededRand(i * 5) * 0.12,
      duration: 20 + seededRand(i * 11) * 25,
      delay: -(seededRand(i * 17) * 20),
      driftX: (seededRand(i * 2) - 0.5) * 130,
      driftY: (seededRand(i * 4) - 0.5) * 110,
      depth: 0.3 + seededRand(i * 9) * 1.4,   // 0.3 – 1.7
      rotation: (seededRand(i * 6) - 0.5) * 10,
    }));
  }, []);

  // 🚫 Don't render anything on mobile / tablet — the animation lags heavily
  // and makes typing in the form very difficult on touch devices.
  if (isMobile) return null;

  return (
    <>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Space+Mono:wght@400;700&display=swap');

        @keyframes floatName {
          0%   { transform: translate(0px, 0px); }
          25%  { transform: translate(var(--dx1), var(--dy1)); }
          50%  { transform: translate(var(--dx2), var(--dy2)); }
          75%  { transform: translate(var(--dx1), calc(var(--dy2) * 0.5)); }
          100% { transform: translate(0px, 0px); }
        }

        @keyframes redGlow {
          0%, 100% {
            text-shadow:
              0 0 6px rgba(255,59,48,0.8),
              0 0 16px rgba(255,59,48,0.5),
              0 0 32px rgba(255,59,48,0.3);
          }
          50% {
            text-shadow:
              0 0 10px rgba(255,59,48,1),
              0 0 28px rgba(255,59,48,0.75),
              0 0 55px rgba(255,59,48,0.4),
              0 0 90px rgba(255,59,48,0.15);
          }
        }

        .fn-float {
          animation: floatName var(--dur) var(--delay) ease-in-out infinite;
          will-change: transform;
        }

        .fn-red {
          font-family: 'Cinzel Decorative', serif;
          font-weight: 700;
          letter-spacing: 0.06em;
          animation: floatName var(--dur) var(--delay) ease-in-out infinite,
                     redGlow 3s ease-in-out infinite;
          will-change: transform, text-shadow;
        }

        .fn-other {
          font-family: 'Space Mono', monospace;
          font-weight: 400;
          letter-spacing: 0.04em;
        }
      `}</style>

      <div className="absolute inset-0 overflow-hidden pointer-events-none z-0">
        {items.map((item, i) => (
          /* Outer wrapper handles cursor parallax */
          <div
            key={i}
            style={{
              position: 'absolute',
              left: `${item.x}%`,
              top: `${item.y}%`,
              transform: `translate(${mouse.x * item.depth * 28}px, ${mouse.y * item.depth * 22}px) rotate(${item.rotation}deg)`,
              transition: 'transform 0.18s ease-out',
            }}
          >
            {/* Inner span handles the float animation */}
            <span
              className={item.isRed ? 'fn-red' : 'fn-float fn-other'}
              style={{
                display: 'block',
                fontSize: `${item.size}px`,
                opacity: item.opacity,
                color: item.isRed ? '#ff3b30' : '#c8d4da',
                whiteSpace: 'nowrap',
                '--dur': `${item.duration}s`,
                '--delay': `${item.delay}s`,
                '--dx1': `${item.driftX}px`,
                '--dy1': `${item.driftY}px`,
                '--dx2': `${-item.driftX * 0.5}px`,
                '--dy2': `${item.driftY * 0.7}px`,
              } as React.CSSProperties}
            >
              {item.name}
            </span>
          </div>
        ))}
      </div>
    </>
  );
};

export default FloatingNames;
