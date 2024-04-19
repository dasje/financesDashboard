import React, { useState } from "react";
import type { FormProps } from "antd";
import { Alert, Button, Checkbox, Form, Input } from "antd";
import { Card, Space } from "antd";
import { ValidateStatus } from "antd/es/form/FormItem";
import { handleLogin } from "../api/auth";
import { useNavigate } from "react-router-dom";

type FieldType = {
  username?: string;
  password?: string;
  remember?: string;
};

const emailRegex: RegExp = /^[\w\-.]+@([\w-]+\.)+[\w-]{2,}$/;
const minMaxLength: RegExp = /^[\s\S]{8,32}$/;
const upper: RegExp = /[A-Z]/;
const lower: RegExp = /[a-z]/;
const number: RegExp = /[0-9]/;
const special: RegExp = /[ !"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~]/;

const onFinish: FormProps<FieldType>["onFinish"] = (values) => {
  console.log("Success:", values);
};

const onFinishFailed: FormProps<FieldType>["onFinishFailed"] = (errorInfo) => {
  console.log("Failed:", errorInfo);
};

const Login = () => {
  const navigate = useNavigate();
  const [userEmail, setUserEmail] = useState<string>("");
  const [userPassword, setUserPassword] = useState<string>("");
  const [emailEnterStatus, setEmailEnterStatus] = useState<ValidateStatus>("");
  const [passwordEnterStatus, setPasswordEnterStatus] =
    useState<ValidateStatus>("");
  const [showErrorMessage, setShowErrorMessage] = useState<boolean>(false);
  const [errorMessage, setErrorMessage] = useState<string>("");

  const emailValidation = (email: string) => {
    return emailRegex.test(email);
  };
  const passwordValidation = (password: string) => {
    if (
      minMaxLength.test(password) &&
      upper.test(password) &&
      lower.test(password) &&
      number.test(password) &&
      special.test(password)
    ) {
      return true;
    } else {
      return false;
    }
  };

  const handleNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    setUserEmail(e.target.value);
    if (!emailValidation(e.target.value)) {
      setEmailEnterStatus("warning");
    } else {
      setEmailEnterStatus("success");
    }
  };
  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    setUserPassword(e.target.value);
    if (!passwordValidation(e.target.value)) {
      setPasswordEnterStatus("warning");
    } else {
      setPasswordEnterStatus("success");
    }
  };

  const handleSubmitButton = async () => {
    if (emailValidation(userEmail) && passwordValidation(userPassword)) {
      console.log("Everything checks out");
      const res = await handleLogin({
        email: userEmail,
        password: userPassword,
      });
      switch (res) {
        case "success":
          navigate("/no-data");
          break;
        case "Incorrect email or password.":
          setErrorMessage(res);
          setShowErrorMessage(true);
          break;
      }
    } else {
      console.log("Cannot proceed");
    }
  };
  return (
    <Space direction="vertical" size={16}>
      <Card
        title="Login"
        extra={<a href={"/signup"}>Sign Up</a>}
        style={{ width: 300 }}
      >
        <Form
          name="basic"
          labelCol={{ span: 8 }}
          wrapperCol={{ span: 16 }}
          style={{ maxWidth: 600 }}
          initialValues={{ remember: true }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item<FieldType>
            label="Email"
            name="username"
            validateStatus={emailEnterStatus}
            hasFeedback
            rules={[{ required: true, message: "Please input your email!" }]}
          >
            <Input
              onChange={(e) => handleNameChange(e)}
              id={emailEnterStatus}
            />
          </Form.Item>

          <Form.Item<FieldType>
            label="Password"
            name="password"
            validateStatus={passwordEnterStatus}
            hasFeedback
            rules={[{ required: true, message: "Please enter a password!" }]}
          >
            <Input.Password
              onChange={(e) => handlePasswordChange(e)}
              id={passwordEnterStatus}
            />
          </Form.Item>

          <Form.Item<FieldType>
            name="remember"
            valuePropName="checked"
            wrapperCol={{ offset: 8, span: 16 }}
          >
            <Checkbox>Remember me</Checkbox>
          </Form.Item>

          {showErrorMessage && (
            <Form.Item wrapperCol={{ offset: 6, span: 16 }}>
              <Alert showIcon={true} message={errorMessage} type="error" />
            </Form.Item>
          )}

          <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Button
              type="primary"
              htmlType="submit"
              onClick={handleSubmitButton}
            >
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </Space>
  );
};

export default Login;
