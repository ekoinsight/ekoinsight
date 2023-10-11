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
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";

// Material Kit 2 React components
import MKBox from "components/MKBox";
import MKAvatar from "components/MKAvatar";
import MKButton from "components/MKButton";
import MKTypography from "components/MKTypography";

function Profile(idToken) {
  // TODO: Can only get this working with the nesting
  const profile = idToken.idToken;
  return (
    <MKBox component="section" py={{ xs: 6, sm: 12 }}>
      <Container>
        <Grid container item xs={12} justifyContent="center" mx="auto">
          <MKBox mt={{ xs: -16, md: -20 }} textAlign="center">
            <MKAvatar src={profile.picture} alt="profile picture" size="xxl" shadow="xl" />
          </MKBox>
          <Grid container justifyContent="center" py={6}>
            <Grid item xs={12} md={7} mx={{ xs: "auto", sm: 6, md: 1 }}>
              <MKBox display="flex" justifyContent="space-between" alignItems="center" mb={1}>
                <MKTypography variant="h3">Welcome {profile.given_name} !</MKTypography>
                <MKButton variant="outlined" color="info" size="small">
                  Start now !
                </MKButton>
              </MKBox>
              <MKTypography variant="body2" fontWeight="light" color="text">
                The world is in need of your ideas. Take glass bottles for example. We all know they
                should go in the recycling bin, yet they still produce a considerable amount of
                waste. <br />
                <br />
                This is where you come in.<br /><br/>
                Your idea can be as small or as big as you like. It can describe ways families can reduce their waste or make better use of glass bottles past their intended lifecycle, or perhaps it may change the way we deal with certain things on a global scale.
              </MKTypography>
            </Grid>
          </Grid>
        </Grid>
      </Container>
    </MKBox>
  );
}

export default Profile;
