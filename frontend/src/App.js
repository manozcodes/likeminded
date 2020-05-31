import React from "react";
import { Menu, Form, Input, Button } from "antd";
import "antd/dist/antd.css";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header>
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
                    <b>Sign Up</b>
                  </a>
                </Menu.Item>
              </Menu>
            </div>
          </div>
        </nav>
        <section id="hero">
          <div className="container">
            <div className="row">
              <div className="col-md-7 content-box hero-content">
                <h1>
                  Meet People, Who Shares <b>Similar Interest.</b>
                </h1>
                <p>Do something awesomeness together.</p>
                <br />
                <br />
                <Form name="horizontal_login" layout="inline">
                  <Form.Item
                    name="username"
                    rules={[
                      {
                        required: true,
                        message: "Please input your username!",
                      },
                    ]}
                  >
                    <Input placeholder="Username" />
                  </Form.Item>
                  <Form.Item
                    name="password"
                    rules={[
                      {
                        required: true,
                        message: "Please input your password!",
                      },
                    ]}
                  >
                    <Input type="password" placeholder="Password" />
                  </Form.Item>
                  <Form.Item>
                    <Button type="primary" htmlType="submit">
                      <a href="">Log in</a>
                    </Button>
                  </Form.Item>
                </Form>
                <b className="dont-have">
                  <a href="">Don't have account?</a>
                </b>
              </div>
              <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 hero-content">
                {/* <Form name="basic">
                  <Form.Item
                    name="username"
                    initialValue="Username"
                    rules={[
                      {
                        required: true,
                        message: "Please input your username!",
                      },
                    ]}
                  >
                    <Input />
                  </Form.Item>

                  <Form.Item
                    name="password"
                    initialValue="Password"
                    rules={[
                      {
                        required: true,
                        message: "Please input your password!",
                      },
                    ]}
                  >
                    <Input />
                  </Form.Item>
                  <Form.Item>
                    <Button type="primary" htmlType="submit">
                      <a href="">Submit</a>
                    </Button>
                  </Form.Item>
                </Form> */}
              </div>
            </div>
          </div>
        </section>
      </header>
    </div>
  );
}

export default App;
