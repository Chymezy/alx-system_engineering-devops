// // Migrate App.js to App.jsx
// import React from 'react';
// import { Route, Routes } from 'react-router-dom';  // Ensure correct import from react-router-dom
// import LoginForm from './components/LoginForm';
// import RegisterForm from './components/RegisterForm';
// import EnergyRecordList from './components/EnergyRecordList';
// import EnergyRecordForm from './components/EnergyRecordForm';
// import Analytics from './components/Analytics';

// const App = () => {
//   return (
//     <div className="App">
//       <Routes>
//         <Route path="/login" element={<LoginForm />} />
//         <Route path="/welcome" element={<Welcome />} />
//         <Route path="/register" element={<RegisterForm />} />
//         <Route path="/energy-records" element={<EnergyRecordList />} />
//         <Route path="/add-energy-record" element={<EnergyRecordForm />} />
//         <Route path="/analytics" element={<Analytics />} /> 
//         <Route path="/" element={<div>Home</div>} />
//       </Routes>
//     </div>
//   );
// };

// export default App;

// src/App.jsx

// src/App.jsx

// src/App.jsx

// src/App.jsx

// src/App.jsx

import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import LoginForm from './components/LoginForm';
import Welcome from './components/Welcome';

const App = () => {
  return (
    <div className="App">
      <Navbar />
      <div style={{ paddingBottom: '60px' }}> {/* Add padding to avoid footer overlap */}
        <Routes>
          <Route path="/login" element={<LoginForm />} />
          <Route path="/welcome" element={<Welcome />} />
          <Route path="/" element={<div>Home</div>} />
        </Routes>
      </div>
      <Footer />
    </div>
  );
};

export default App;
