import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import EnergyRecordForm from './components/EnergyRecordForm';
import EnergyRecordList from './components/EnergyRecordList';
import Analytics from './components/Analytics';
import './App.css';

function App() {
  return (
    <div className="App">
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/add-record" component={EnergyRecordForm} />
        <Route path="/energy-records" component={EnergyRecordList} />
        <Route path="/analytics" component={Analytics} />
      </Switch>
    </div>
  );
}

export default App;

