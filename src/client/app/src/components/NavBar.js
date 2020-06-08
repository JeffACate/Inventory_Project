import React from "react";
import { BrowserRouter, Link, Route } from "react-router-dom";
import AllContacts from "./AllContacts";
import Home from "./Home";

  

export default function NavBar() {
    return (
    <BrowserRouter>
        <div className="App">
          <header className="App-header">
            <h1>GoodThings</h1>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/AllContacts">AllContacts</Link>
              </li>
            </ul>
          </header>
          <main>
            <Route exact path="/">
            </Route>
              <Route path="/" component={Home} exact />
              <Route path="/AllContacts" component={AllContacts} />
          </main>
        </div>
      </BrowserRouter>
    );
}