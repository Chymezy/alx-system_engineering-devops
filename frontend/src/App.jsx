import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './components/Home';
import Features from './components/Features';
import About from './components/About';
import LoginForm from './components/LoginForm';
import Welcome from './components/Welcome';

const App = () => {
  return (
    <div className="App">
      <Navbar />
      <div style={{ paddingBottom: '60px' }}> {/* Add padding to avoid footer overlap */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path='/features' element={<Features />} />
          <Route path="/about" element={<About />} />
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

// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Navbar from './components/Navbar';
// import Footer from './components/Footer';
// import Home from './components/Home';
// import Features from './components/Features';
// import About from './components/About';
// import LoginForm from './components/LoginForm';
// import Welcome from './components/Welcome';


// const App = () => {
//   return (
//     <Router>
//       <Navbar />
//       <div className="main-content">
//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/features" element={<Features />} />
//           <Route path="/about" element={<About />} />
//           <Route path="/login" element={<LoginForm />} />
//           <Route path="/welcome" element={<Welcome />} />
//         </Routes>
//       </div>
//       <Footer />
//     </Router>
//   );
// };

// export default App;
