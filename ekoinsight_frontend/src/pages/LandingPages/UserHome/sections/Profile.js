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
    <MKBox component="section" mb={0} pb={0} pt={{ xs: 6, sm: 12 }}>
      <Container>
        <Grid container item xs={12} justifyContent="center">
          <MKBox mt={{ xs: 0, md: -20 }} mb={0} textAlign="center">
            <MKAvatar src={profile.picture} alt="profile picture" size="xxl" shadow="xl" />
          </MKBox>
          <Grid container justifyContent="center" py={2}>
            <Grid item xs={12} md={7} mx={{ xs: "auto", sm: 6, md: 1 }}>
              <MKBox display="flex" justifyContent="space-between" alignItems="center" mb={0}>
                <MKTypography variant="h3">Welcome {profile.given_name} !</MKTypography>
                {/* <MKButton variant="outlined" color="info" size="small">
                  Start now !
                </MKButton> */}
              </MKBox>
            </Grid>
          </Grid>
        </Grid>
      </Container>
    </MKBox>
  );
}

export default Profile;
