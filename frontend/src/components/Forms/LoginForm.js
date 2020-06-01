import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import { Form, Input, Button } from "antd";

export const LoginForm = () => {
  return (
    <Fragment>
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
        <a href="">
          <Link to="/signup">Don't have account?</Link>
        </a>
      </b>
    </Fragment>
  );
};
