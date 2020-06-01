import React, { Fragment } from "react";
import { NavBar } from "../../Header/NavBar";
import { TopHeader } from "./TopHeader";

export const HomePage = () => {
  return (
    <Fragment>
      <NavBar />
      <TopHeader />
    </Fragment>
  );
};
