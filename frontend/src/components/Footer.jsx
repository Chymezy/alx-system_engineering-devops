// // src/components/Footer.jsx

// import React from 'react';
// import { Box, Typography } from '@mui/material';

// const Footer = () => {
//   return (
//     <Box
//       component="footer"
//       sx={{
//         display: 'flex',
//         justifyContent: 'center',
//         alignItems: 'center',
//         padding: '10px',
//         backgroundColor: '#f5f5f5',
//         position: 'fixed',
//         bottom: 0,
//         width: '100%',
//       }}
//     >
//       <Typography variant="body2" color="textSecondary">
//         &copy; {new Date().getFullYear()} Energy Manager. All rights reserved.
//       </Typography>
//     </Box>
//   );
// };

// export default Footer;

// src/components/Footer.jsx

// src/components/Footer.jsx

// src/components/Footer.jsx

import React from 'react';
import { Box, Typography, Link } from '@mui/material';
import SolarPowerIcon from '../assets/solar-power.svg';
import ElectricityIcon from '../assets/electricity.svg';
import EfficiencyIcon from '../assets/efficiency.svg';

const Footer = () => {
  return (
    <Box
      component="footer"
      sx={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '20px',
        backgroundColor: '#f5f5f5',
        width: '100%',
        boxShadow: '0px -2px 8px rgba(0, 0, 0, 0.1)',
        position: 'relative', // Change from fixed to relative
        bottom: 0,
        mt: 'auto', // Ensure it appears at the bottom after all content
      }}
    >
      <Typography variant="body2" color="textSecondary" style={{ display: 'flex', alignItems: 'center' }}>
        <img src={SolarPowerIcon} alt="Solar Power" style={{ height: '20px', marginRight: '10px' }} />
        <img src={ElectricityIcon} alt="Electricity" style={{ height: '20px', marginRight: '10px' }} />
        <img src={EfficiencyIcon} alt="Efficiency" style={{ height: '20px', marginRight: '10px' }} />
        &copy; {new Date().getFullYear()} Energy Manager. All rights reserved.
      </Typography>
      <Box>
        <Link href="#" color="inherit" sx={{ mx: 1 }}>
          Privacy Policy
        </Link>
        <Link href="#" color="inherit" sx={{ mx: 1 }}>
          Terms of Service
        </Link>
        <Link href="#" color="inherit" sx={{ mx: 1 }}>
          Contact Us
        </Link>
      </Box>
    </Box>
  );
};

export default Footer;
