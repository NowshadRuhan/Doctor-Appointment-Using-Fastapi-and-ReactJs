import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar = () =>{

    return (
        <nav className="navbar navbar-expand-sm navbar-dark bg-dark">
            <div className="container-fluid">
                <NavLink className="navbar-brand" to="/">Book Appointment</NavLink>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="mynavbar">
                <ul className="navbar-nav me-auto">
                    <li className="nav-item">
                    <NavLink className="nav-link" exact to="/">Home</NavLink>
                    </li>
                    <li className="nav-item">
                    <NavLink className="nav-link" exact to="/Signup">Signup</NavLink>
                    </li>
                    <li className="nav-item">
                    <NavLink className="nav-link" exact to="/Signin">Signin</NavLink>
                    </li>
                </ul>
                <form className="d-flex">
                    <input className="form-control me-2" type="text" placeholder="Search" />
                    <button className="btn btn-primary" type="button">Search</button>
                </form>
                </div>
            </div>
            </nav>
  

    );

}


export default Navbar;