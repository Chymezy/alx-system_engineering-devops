import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import EnergyRecordList from './components/EnergyRecordList';
import EnergyRecordForm from './components/EnergyRecordForm';
import Analytics from './components/Analytics';

// Importance: Defines the main application component and sets up routes for different views.

const App = () => {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login" component={LoginForm} />
          <Route path="/register" component={RegisterForm} />
          <Route path="/energy-records" component={EnergyRecordList} />
          <Route path="/add-energy-record" component={EnergyRecordForm} />
          <Route path="/analytics" component={Analytics} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;

