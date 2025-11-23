module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        travel: {
          blue: '#0A3D62',
          blueLight: '#1B6CA8',
          orange: '#FF7F11',
          beige: '#F5E6D3',
          charcoal: '#2E2E2E'
        }
      },
      fontFamily: {
        sans: ['Inter', 'Nunito Sans', 'system-ui', 'sans-serif']
      },
      boxShadow: {
        soft: '0 4px 12px rgba(10,61,98,0.08)',
        elevate: '0 6px 20px rgba(10,61,98,0.12)'
      }
    },
  },
  plugins: [],
};
