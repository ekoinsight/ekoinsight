/**
=========================================================
* Material Kit 2 React - v2.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-kit-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

import { useEffect, useState } from "react";

// react-router-dom components
import { useNavigate } from "react-router-dom";

// @mui material components
import Card from "@mui/material/Card";
import Grid from "@mui/material/Grid";

// Material Kit 2 React components
import MKButton from "components/MKButton";
import MKBox from "components/MKBox";
import MKTypography from "components/MKTypography";

// Material Kit 2 React example components
import DefaultNavbar from "examples/Navbars/DefaultNavbar";
import SimpleFooter from "examples/Footers/SimpleFooter";

// Material Kit 2 React page layout routes
import routes from "routes";

import jwtDecode from "jwt-decode";

// Images
import bgImage from "assets/images/bg-sign-in-basic.jpeg";

// Ouath
import { GoogleLogin, googleLogout } from "@react-oauth/google";

export function CheckIsLoggedIn(data) {
  const navigate = useNavigate();

  if (data) {
    console.log("Confirmed token was present.");
    console.log(data);

    let decodedToken = jwtDecode(data.credential);
    console.log("Decoded token", decodedToken);
    let currentDate = new Date();

    if (decodedToken.exp * 1000 < currentDate.getTime()) {
      console.log("Token expired.");
      useEffect(() => {
        navigate("/pages/authentication/sign-in");
      });
    } else {
      console.log("Valid token");
      return decodedToken;
    }
  } else {
    console.log("Could not find token, ");
    useEffect(() => {
      navigate("/pages/authentication/sign-in");
    });
  }
}

function SignInBasic() {
  const navigate = useNavigate();
  const [googleUser, setGoogleUser] = useState([]);
  console.log(googleUser);
  // console.log(userProfile);

  const handleSuccessLogin = (resp) => {
    setGoogleUser(resp);
    console.log("Login successful !");
    console.log(resp);
    navigate("/pages/landing-pages/user-home", { state: JSON.stringify(resp) });
  };

  const handleErrorLogin = (err) => {
    console.log("Login error !" + err);
  };

  function handleLogout() {
    googleLogout();
  }

  return (
    <>
      <DefaultNavbar
        routes={routes}
        action={{
          type: "internal",
          route: "/Home",
          label: "Home",
          color: "info",
        }}
        sticky
      />
      <MKBox
        position="absolute"
        top={0}
        left={0}
        zIndex={1}
        width="100%"
        minHeight="100vh"
        sx={{
          backgroundImage: ({ functions: { linearGradient, rgba }, palette: { gradients } }) =>
            `${linearGradient(
              rgba(gradients.dark.main, 0.6),
              rgba(gradients.dark.state, 0.6)
            )}, url(${bgImage})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          backgroundRepeat: "no-repeat",
        }}
      />
      <MKBox px={1} width="100%" height="100vh" mx="auto" position="relative" zIndex={2}>
        <Grid container spacing={1} justifyContent="center" alignItems="center" height="100%">
          <Grid item xs={11} sm={9} md={5} lg={4} xl={3}>
            <Card>
              <MKBox
                variant="gradient"
                bgColor="info"
                borderRadius="lg"
                coloredShadow="info"
                mx={2}
                mt={-3}
                p={2}
                mb={1}
                textAlign="center"
              >
                <MKTypography variant="h4" fontWeight="medium" color="white" mt={1}>
                  Sign in
                </MKTypography>
              </MKBox>
              <MKBox pt={4} pb={3} px={3}>
                <MKBox component="form" role="form">
                  <GoogleLogin
                    text="continue_with"
                    size="large"
                    onSuccess={handleSuccessLogin}
                    onError={handleErrorLogin}
                  />
                  {/* <MKBox textAlign="center" mt={4} mb={1}>
                    <MKButton onClick={handleLogout} size="small" variant="gradient" color="info">
                      Logout
                    </MKButton>
                  </MKBox> */}
                  <MKBox mt={3} mb={1} textAlign="center"></MKBox>
                </MKBox>
              </MKBox>
            </Card>
          </Grid>
        </Grid>
      </MKBox>
      <MKBox width="100%" position="absolute" zIndex={2} bottom="1.625rem">
        <SimpleFooter light />
      </MKBox>
    </>
  );
}

export default SignInBasic;
