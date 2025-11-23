import React from 'react';
import NavBar from './NavBar';

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div className="min-h-screen flex flex-col">
    <NavBar />
    {children}
    <nav className="mt-auto py-5 backdrop-blur bg-white/5 border-t border-travel-blue/20 text-center text-[11px] text-travel-beige/70 flex flex-col gap-1">
      <div>© {new Date().getFullYear()} Multi-Agent Tourism Planner</div>
      <div className="flex items-center justify-center gap-4">
        <a href="#features" className="hover:text-white transition">Features</a>
        <a href="#about" className="hover:text-white transition">About</a>
        <a href="https://openmeteo.com" target="_blank" rel="noreferrer" className="hover:text-white transition">Weather API</a>
        <a href="https://overpass-api.de" target="_blank" rel="noreferrer" className="hover:text-white transition">Attractions Data</a>
      </div>
    </nav>
  </div>
);

export default Layout;
