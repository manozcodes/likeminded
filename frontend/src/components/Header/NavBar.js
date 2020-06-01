import React from "react";
import { Menu, Button } from "antd";
import { Link } from "react-router-dom";

export const NavBar = () => {
  return (
    <nav className="navbar navbar-default navbar-expand-lg fixed-top custom-navbar">
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="icon ion-md-menu"></span>
      </button>
      <img
        src="images/logo.png"
        className="img-fluid nav-logo-mobile"
        alt="Company Logo"
      />
      <div className="collapse navbar-collapse" id="navbarNavDropdown">
        <div className="container">
          <Link to="/">
            <img
              src="https://raw.githubusercontent.com/manozcodes/likeminded/master/frontend/src/images/logo.png"
              height="35"
              width="180"
            />
          </Link>

          <Menu className="navbar-nav ml-auto nav-right">
            <Menu.Item className="nav-item nav-custom-link">
              <a className="nav-link" href="#">
                About Us
              </a>
            </Menu.Item>

            <Menu.Item className="nav-item nav-custom-link">
              <a className="nav-link" href="#">
                How it Works
              </a>
            </Menu.Item>
            <Menu.Item className="nav-item nav-custom-link">
              <a className="nav-link" href="#">
                Top Profiles
              </a>
            </Menu.Item>
            <Menu.Item className="nav-item">
              <Button type="primary" htmlType="submit">
                <Link to="/signup">Sign Up</Link>
              </Button>
            </Menu.Item>
          </Menu>
        </div>
      </div>
    </nav>
  );
};
