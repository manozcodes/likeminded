import React from "react";
import { LoginForm } from "../../Forms/LoginForm";

export const TopHeader = () => {
  return (
    <section id="hero">
      <div className="container">
        <div className="row">
          <div className="col-md-7 content-box hero-content">
            <h1>
              Meet People, Who Shares <b>Similar Interest.</b>
            </h1>
            <p className="mb-3">Do something awesomeness together.</p>
            <LoginForm />
          </div>
          <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 hero-content"></div>
        </div>
      </div>
    </section>
  );
};
