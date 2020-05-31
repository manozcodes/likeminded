import React from "react";
import "./App.css";
import { Menu } from "antd";

function App() {
  return (
    <div className="App">
      <nav class="navbar navbar-default navbar-expand-lg fixed-top custom-navbar">
        <button
          class="navbar-toggler"
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
          class="img-fluid nav-logo-mobile"
          alt="Company Logo"
        />
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <div class="container">
            <Menu className="navbar-nav ml-auto test">
              <Menu.Item className="nav-item nav-custom-link">
                <a className="nav-link" href="#">
                  Home
                </a>
              </Menu.Item>

              <Menu.Item className="nav-item nav-custom-link">
                <a className="nav-link" href="#">
                  Features
                </a>
              </Menu.Item>
              <Menu.Item className="nav-item nav-custom-link">
                <a className="nav-link" href="#">
                  Find Mentors
                </a>
              </Menu.Item>
              <Menu.Item className="nav-item nav-custom-link">
                <a className="nav-link" href="#">
                  Publications
                </a>
              </Menu.Item>
              <Menu.Item className="nav-item nav-custom-link">
                <a className="nav-link" href="#">
                  About Us
                </a>
              </Menu.Item>
            </Menu>
            <ul
              class="navbar-nav ml-auto nav-right"
              data-easing="easeInOutExpo"
              data-speed="1250"
              data-offset="65"
            >
              {/* <li class="nav-item nav-custom-link">
                <a class="nav-link" href="index.html">
                  Home <i class="icon ion-ios-arrow-forward icon-mobile"></i>
                </a>
              </li>
              <li class="nav-item nav-custom-link">
                <a class="nav-link" href="#marketing">
                  Features{" "}
                  <i class="icon ion-ios-arrow-forward icon-mobile"></i>
                </a>
              </li>
              <li class="nav-item nav-custom-link">
                <a class="nav-link" href="#testimonials">
                  Testimonials
                  <i class="icon ion-ios-arrow-forward icon-mobile"></i>
                </a>
              </li>
              <li class="nav-item nav-custom-link">
                <a class="nav-link" href="#pricing">
                  Pricing <i class="icon ion-ios-arrow-forward icon-mobile"></i>
                </a>
              </li>
              <li class="nav-item nav-custom-link btn btn-demo-small">
                <a class="nav-link" href="#">
                  Sign Up
                  <i class="icon ion-ios-arrow-forward icon-mobile"></i>
                </a>
              </li> */}
              <img
                src="images/logo.png"
                // class="img-fluid nav-logo-mobile"
                alt="Company Logo"
                class="test-logo"
              />
              <Menu className="navbar-nav ml-auto nav-right">
                <Menu.Item className="nav-item nav-custom-link">
                  <a className="nav-link" href="#">
                    Home
                  </a>
                </Menu.Item>

                <Menu.Item className="nav-item nav-custom-link">
                  <a className="nav-link" href="#">
                    Features
                  </a>
                </Menu.Item>
                <Menu.Item className="nav-item nav-custom-link">
                  <a className="nav-link" href="#">
                    Find Mentors
                  </a>
                </Menu.Item>
                <Menu.Item className="nav-item nav-custom-link">
                  <a className="nav-link" href="#">
                    Publications
                  </a>
                </Menu.Item>
                <Menu.Item className="nav-item nav-custom-link">
                  <a className="nav-link" href="#">
                    About Us
                  </a>
                </Menu.Item>
                <Menu.Item className="nav-item nav-custom-link btn btn-demo-small">
                  <a className="nav-link" href="#">
                    Sign Up
                  </a>
                </Menu.Item>
              </Menu>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default App;
