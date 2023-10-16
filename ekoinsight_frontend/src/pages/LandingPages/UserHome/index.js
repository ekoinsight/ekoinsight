/*
=========================================================
* Material Kit 2 React - v2.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-kit-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// @mui material components
import Card from "@mui/material/Card";

// Material Kit 2 React components
import MKBox from "components/MKBox";

// Material Kit 2 React examples
import DefaultNavbar from "examples/Navbars/DefaultNavbar";

// UserHome page sections
import Profile from "pages/LandingPages/UserHome/sections/Profile";
import Tamagotchi from "pages/LandingPages/UserHome/sections/Tamagotchi";
import Posts from "pages/LandingPages/UserHome/sections/Posts";
import Contact from "pages/LandingPages/UserHome/sections/Contact";
import Footer from "pages/LandingPages/UserHome/sections/Footer";

// Routes
import routes from "routes";

// Images
import bgImage from "assets/images/city-profile.jpg";

import { useLocation } from "react-router-dom";

import { CheckIsLoggedIn } from "pages/LandingPages/SignIn";

function UserHome() {
  const location = useLocation();
  const data = JSON.parse(location.state);
  console.log("data below");
  console.log(data);

  const idToken = CheckIsLoggedIn(data);
  console.log("idToken in userhome", idToken);

  if (idToken) {
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
        <MKBox bgColor="white">
          <MKBox
            minHeight="25rem"
            width="100%"
            sx={{
              backgroundImage: ({ functions: { linearGradient, rgba }, palette: { gradients } }) =>
                `${linearGradient(
                  rgba(gradients.dark.main, 0.8),
                  rgba(gradients.dark.state, 0.8)
                )}, url(${bgImage})`,
              backgroundSize: "cover",
              backgroundPosition: "center",
              display: "grid",
              placeItems: "center",
            }}
          />
          <Card
            sx={{
              p: 2,
              mx: { xs: 2, lg: 3 },
              mt: -8,
              mb: 1,
              backgroundColor: ({ palette: { white }, functions: { rgba } }) =>
                rgba(white.main, 0.8),
              backdropFilter: "saturate(200%) blur(30px)",
              boxShadow: ({ boxShadows: { xxl } }) => xxl,
            }}
          >
            <Profile idToken={idToken} />
            <Tamagotchi idToken={idToken} />
          </Card>
        </MKBox>
      </>
    );
  } else {
    return <h1>Not Loaded</h1>;
  }
}

export default UserHome;
