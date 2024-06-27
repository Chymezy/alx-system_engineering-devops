// Migrate App.js to App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import EnergyRecordList from './components/EnergyRecordList';
import EnergyRecordForm from './components/EnergyRecordForm';
import Analytics from './components/Analytics';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/energy-records" element={<EnergyRecordList />} />
          <Route path="/add-energy-record" element={<EnergyRecordForm />} />
          <Route path="/analytics" element={<Analytics />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;

// import React from 'react'
// import './App.css'

// function App() {
//   return (
//     <div className="App">
//       <h1>Hello Vite + React!</h1>
//     </div>
//   )
// }

// export default App
