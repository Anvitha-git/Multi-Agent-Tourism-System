import React from 'react';

const Loader: React.FC = () => (
  <div className="travel-loader-wrapper">
    <div className="travel-loader-track" />
    <div className="travel-cloud" />
    <div className="travel-cloud" />
    <div className="travel-cloud" />
    <div className="travel-cloud" />
    <svg className="travel-loader-plane" width="38" height="20" viewBox="0 0 48 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M2 13c10 0 14-2 18-5l6-5 4 1-4 7h10l2 2-2 2H26l4 7-4 1-6-5c-4-3-8-5-18-5v-2Z" fill="#FF7F11" opacity="0.9" />
      <circle cx="33" cy="12" r="2" fill="#fff" />
    </svg>
    <div className="absolute left-0 top-full mt-1 text-xs text-travel-beige/70 tracking-wide">Planning route...</div>
  </div>
);

export default Loader;
