import React from "react";
import { Form, Input, Button } from "antd";
import { Link } from "react-router-dom";

export const SignupForm = () => {
  return (
    <div className="signup-form-parent">
      <Form
        name="normal_login"
        className="signup-form"
        initialValues={{ remember: true }}
      >
        <img
          src="https://raw.githubusercontent.com/manozcodes/likeminded/master/frontend/src/images/logo.png"
          height="35"
          width="180"
          className="mb-4"
        />
        <Form.Item
          name="username"
          rules={[{ required: true, message: "Please input your Username!" }]}
        >
          <Input placeholder="Username" />
        </Form.Item>
        <Form.Item
          name="fullname"
          rules={[{ required: true, message: "Please input your Username!" }]}
        >
          <Input placeholder="Full Name" />
        </Form.Item>
        <Form.Item
          name="Email"
          rules={[{ required: true, message: "Please input your Username!" }]}
        >
          <Input placeholder="Email" />
        </Form.Item>
        <Form.Item
          name="password"
          rules={[{ required: true, message: "Please input your Password!" }]}
        >
          <Input type="password" placeholder="Password" />
        </Form.Item>
        <Form.Item>
          Already have a account?
          <Link to="/" className="login-form ml-1">
            Login
          </Link>
        </Form.Item>

        <Form.Item>
          <Button
            type="primary"
            htmlType="submit"
            className="login-form-button"
          >
            Register
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};
