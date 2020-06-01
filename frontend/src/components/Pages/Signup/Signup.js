import React, { Fragment } from "react";
import { NavBar } from "../../Header/NavBar";
import { SignupForm } from "../../Forms/SignupForm";

export const Signup = () => {
  return (
    <Fragment>
      <NavBar />
      <div className="signup-top">
        <SignupForm />
      </div>
    </Fragment>
  );
};
