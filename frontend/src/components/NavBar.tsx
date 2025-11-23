import React, { useState } from 'react';

const NavBar: React.FC = () => {
  const [open, setOpen] = useState(false);
  return (
    <nav className="w-full backdrop-blur bg-white/10 border-b border-travel-blue/20 sticky top-0 z-50">
      <div className="travel-container flex items-center justify-between py-3">
        <a href="#" className="text-travel-beige/90 font-semibold tracking-wide text-sm md:text-base flex items-center gap-2">
          <span className="inline-block w-2.5 h-2.5 rounded-full bg-travel-orange animate-pulse" />
          Multi-Agent Tourism Planner
        </a>
        <button aria-label="Toggle navigation" onClick={() => setOpen(o => !o)} className="md:hidden text-travel-beige/80 hover:text-white transition focus:outline-none focus:ring-2 focus:ring-travel-orange rounded px-2 py-1">
          {open ? (
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" /></svg>
          ) : (
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="3" y1="6" x2="21" y2="6" /><line x1="3" y1="12" x2="21" y2="12" /><line x1="3" y1="18" x2="21" y2="18" /></svg>
          )}
        </button>
        <ul className="hidden md:flex items-center gap-6 text-xs md:text-sm font-medium">
          <li><a href="#features" className="text-travel-beige/80 hover:text-white transition">Features</a></li>
          <li><a href="#about" className="text-travel-beige/80 hover:text-white transition">About</a></li>
          <li><a href="https://openstreetmap.org" target="_blank" rel="noreferrer" className="text-travel-beige/60 hover:text-white transition">Data Sources</a></li>
        </ul>
      </div>
      {open && (
        <div className="md:hidden px-4 pb-4 animate-fadeIn">
          <ul className="flex flex-col gap-3 text-sm font-medium">
            <li><a onClick={() => setOpen(false)} href="#features" className="text-travel-beige/80 hover:text-white transition">Features</a></li>
            <li><a onClick={() => setOpen(false)} href="#about" className="text-travel-beige/80 hover:text-white transition">About</a></li>
            <li><a onClick={() => setOpen(false)} href="https://openstreetmap.org" target="_blank" rel="noreferrer" className="text-travel-beige/60 hover:text-white transition">Data Sources</a></li>
          </ul>
        </div>
      )}
    </nav>
  );
};

export default NavBar;
