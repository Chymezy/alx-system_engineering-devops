// import { defineConfig } from 'vite';
// import react from '@vitejs/plugin-react';
// import svgr from '@svgr/rollup';
// import dotenv from 'dotenv';

// dotenv.config();

// export default defineConfig({
//   plugins: [react(), svgr()],
//   server: {
//     port: 3000,
//   },
// });

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import svgr from '@svgr/rollup';
import dotenv from 'dotenv';

dotenv.config();

export default defineConfig({
  plugins: [
    react(),
    svgr({
      svgo: false, // Disable SVGO optimization
    }),
  ],
  server: {
    port: 3000,
  },
});
