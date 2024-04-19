import axios from "axios";
import FormData from "form-data";

const signup_link: string | undefined = process.env.REACT_APP_SIGNUP_URL;
const login_link: string | undefined = process.env.REACT_APP_LOGIN_URL;
console.log(signup_link);

interface LoginInfo {
  email: string;
  password: string;
}

export const handleSignUp = async (user: LoginInfo) => {
  console.log(user);
  try {
    // 👇️ const data: CreateUserResponse
    const { data, status } = await axios.post(signup_link!, user, {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });

    console.log(JSON.stringify(data, null, 4));

    console.log(status);
    if (data.message === "User added.") {
      return data.message;
    }
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.log("error message: ", error.message);
      if (error.response?.data.detail === "User already exists.") {
        return error.response?.data.detail;
      } else if (error.response?.data.detail === "User not added.") {
        return error.response?.data.detail;
      }
    } else {
      console.log("unexpected error: ", error);
      return "An unexpected error occurred";
    }
  }
};

export const handleLogin = async (user: LoginInfo) => {
  console.log(user);
  const formData = new FormData();
  formData.append("username", user.email);
  formData.append("password", user.password);
  try {
    // 👇️ const data: CreateUserResponse
    const { data, status } = await axios.post(login_link!, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    console.log(JSON.stringify(data, null, 4));

    console.log(status);

    const token = data.access_token;
    const expires = data.expires;

    document.cookie = `token=${token}; Max-Age=${expires}`;

    return "success";
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.log("error message: ", error.message);
      if (error.response?.data.detail === "Incorrect email or password.") {
        return error.response?.data.detail;
      }
    } else {
      console.log("unexpected error: ", error);
      return "An unexpected error occurred";
    }
  }
};
