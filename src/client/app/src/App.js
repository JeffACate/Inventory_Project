import React from 'react';
import { BrowserRouter, Router } from "react-router-dom";
import Home from "./components/Home";
import AllContacts from "./components/AllContacts";
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <div>
        <Router component={Home} path="/" exact />
        <Router component={AllContacts} path="/AllContacts" />
        <Router component={Home} path="/" exact />
      </div>
    </BrowserRouter>
  );
}

export default App;
 