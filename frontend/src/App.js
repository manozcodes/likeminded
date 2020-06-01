import React from "react";
import "antd/dist/antd.css";
import "./assets/css/style.css";
import ReactDOM from "react-dom";
import { HashRouter as Router, Switch, Route } from "react-router-dom";
import { HomePage } from "./components/Pages/HomePage/HomePage";
import { Signup } from "./components/Pages/Signup/Signup";

export default function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/signup/" component={Signup} />
        </Switch>
      </Router>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
