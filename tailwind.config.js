/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,svelte,ts}',
  ],
  theme: {
    extend: {
      colors: {
        // Water2Wires Cyberpunk Palette
        'w2w-cyan': '#00E5FF',
        'w2w-pink': '#FF0080',
        'w2w-black': '#0A0A0A',
        'w2w-surface': '#1A1F3A',
        'w2w-card': '#12162B',
        'w2w-text': '#FFFFFF',
        'w2w-muted': '#8B92B2',
        'w2w-success': '#00FF88',
        'w2w-warning': '#FFB800',
        'w2w-danger': '#FF0055',
        // Legacy aliases
        primary: '#00E5FF',
        secondary: '#FF0080',
        surface: '#0A0A0A',
        card: '#1A1F3A',
        success: '#00FF88',
        warning: '#FFB800',
        danger: '#FF0055',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        display: ['Space Grotesk', 'Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite',
        'spin-slow': 'spin 3s linear infinite',
        'circuit-flow': 'circuit-flow 3s linear infinite',
        'glitch': 'glitch 0.3s ease infinite',
        'neon-flicker': 'neon-flicker 2s linear infinite',
        'data-stream': 'data-stream 2s linear infinite',
        'typewriter': 'typewriter 2s steps(40) forwards',
        'blink': 'blink 0.7s infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        'pulse-glow': {
          '0%, 100%': { 
            boxShadow: '0 0 20px rgba(0, 229, 255, 0.3)',
            opacity: '1',
          },
          '50%': { 
            boxShadow: '0 0 40px rgba(0, 229, 255, 0.6)',
            opacity: '0.9',
          },
        },
        'circuit-flow': {
          '0%': { strokeDashoffset: '1000' },
          '100%': { strokeDashoffset: '0' },
        },
        'glitch': {
          '0%, 100%': { transform: 'translate(0)' },
          '20%': { transform: 'translate(-2px, 2px)' },
          '40%': { transform: 'translate(-2px, -2px)' },
          '60%': { transform: 'translate(2px, 2px)' },
          '80%': { transform: 'translate(2px, -2px)' },
        },
        'neon-flicker': {
          '0%, 19%, 21%, 23%, 25%, 54%, 56%, 100%': { 
            opacity: '1',
            textShadow: '0 0 10px #00E5FF, 0 0 20px #00E5FF, 0 0 40px #00E5FF'
          },
          '20%, 24%, 55%': { 
            opacity: '0.8',
            textShadow: 'none'
          },
        },
        'data-stream': {
          '0%': { backgroundPosition: '0% 0%' },
          '100%': { backgroundPosition: '0% 100%' },
        },
        'typewriter': {
          'from': { width: '0' },
          'to': { width: '100%' },
        },
        'blink': {
          '50%': { opacity: '0' },
        },
      },
      backdropBlur: {
        xs: '2px',
      },
      boxShadow: {
        'neon-cyan': '0 0 20px rgba(0, 229, 255, 0.5), 0 0 40px rgba(0, 229, 255, 0.3)',
        'neon-pink': '0 0 20px rgba(255, 0, 128, 0.5), 0 0 40px rgba(255, 0, 128, 0.3)',
        'neon-dual': '0 0 20px rgba(0, 229, 255, 0.3), 0 0 40px rgba(255, 0, 128, 0.2)',
      },
    },
  },
  plugins: [],
};
