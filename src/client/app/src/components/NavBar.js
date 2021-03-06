import React from "react";
import { BrowserRouter, Link, Route } from "react-router-dom";
import AllContacts from "./AllContacts";
import Home from "./Home";

  

export default function NavBar() {
    return (
      <>
      <BrowserRouter>
          <nav className="navbar navbar-expand-lg  mb-3 navbar-dark bg-dark">
            <div className="container">
            <h3 className="nav-brand text-white">Inventory</h3>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
              <ul className="nav navbar-nav center">
                <li className="nav-item">
                  <Link to="/" className="nav-link">Home<span className="sr-only">(current)</span></Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/AllContacts">AllContacts</Link>
                </li>
                {/*<li className="nav-item dropdown">
                  <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Dropdown
                  </a>
                  <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a className="dropdown-item" href="#">Action</a>
                    <a className="dropdown-item" href="#">Another action</a>
                    <div className="dropdown-divider"></div>
                    <a className="dropdown-item" href="#">Something else here</a>
                  </div>
                </li> 
                <li className="nav-item">
                  <a className="nav-link disabled" href="#" tabIndex="-1" aria-disabled="true">Disabled</a>
                </li>*/}
              </ul>
              {/* <form className="form-inline my-2 my-lg-0">
                <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"></input>
                <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
              </form> */}
            </div>
            </div>
          </nav>
          
          
          <main className="container">
              <Route path="/" component={Home} exact />
              <Route path="/AllContacts" component={AllContacts} />
              {/* <Route path="/FindContact" component={FindContact} />
              <Route path="/Contact" component={Contact} /> */}
          </main>


        </BrowserRouter>
        <footer className="footer border-top border-dark bg-dark fixed-bottom p-2 text-white-50">
          <div className="container">
            <div className="row justify-content-center">
              <span>Creator : Jeff A Cate | Images from various <a className="text-white " href="www.unsplash.com">Unsplash</a> artists | &copy; 2020</span>
            </div>
          </div>
        </footer>
        </>
    );
}











//  <ul className="nav">
// <li className="nav-item">
//   <Link to="/" className="nav-link">Home</Link>
// </li>
// <li className="nav-item">
//   <Link to="/AllContacts" className="nav-link">AllContacts</Link>
// </li>
// <li className="nav-item">
//   <Link to="/" className="nav-link">Search</Link>
// </li>
// </ul> 