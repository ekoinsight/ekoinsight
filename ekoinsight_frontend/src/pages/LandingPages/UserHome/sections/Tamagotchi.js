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
import Card from "@mui/material/Card";
import MKInput from "components/MKInput";

import MKAvatar from "components/MKAvatar";
import MKButton from "components/MKButton";
import MKTypography from "components/MKTypography";

import CenteredBlogCard from "examples/Cards/BlogCards/CenteredBlogCard";

import tama_idle from "assets/images/tama_idle.gif";

function Tamagotchi(idToken) {
  // TODO: Can only get this working with the nesting
  const profile = idToken.idToken;
  return (
    <MKBox component="section" mb={0} pt={0} pb={{ xs: 6, sm: 12 }}>
      <Container>
        <Grid container item xs={12} justifyContent="center" mx="auto">
          <Grid container justifyContent="center" py={6}>
            <Grid item xs={12} md={7} mx={{ xs: "auto", sm: 6, md: 1 }}>
              <Card>
                <MKBox position="relative" borderRadius="lg" mx={2} mt={-3}>
                  <MKBox
                    component="img"
                    src={tama_idle}
                    borderRadius="lg"
                    width="100%"
                    position="relative"
                    zIndex={1}
                  />
                  <MKBox
                    borderRadius="lg"
                    shadow="md"
                    width="100%"
                    height="100%"
                    position="absolute"
                    left={0}
                    top={0}
                    sx={{
                      backgroundImage: `url(${tama_idle})`,
                      transform: "scale(0.94)",
                      filter: "blur(12px)",
                      backgroundSize: "cover",
                    }}
                  />
                </MKBox>
                <MKBox p={3} mt={-1} textAlign="center">
                  <MKTypography
                    display="inline"
                    variant="h5"
                    textTransform="capitalize"
                    fontWeight="regular"
                  >
                    Score: 100
                  </MKTypography>
                  <MKBox mt={1} mb={3}>
                    <MKTypography variant="body2" component="p" color="text">
                    Good morning, Tamagotchi Keeper! Your PlanetPal is thriving today. It woke up with a big smile, well-fed, and full of energy. It&apos;s been living a green and happy life with you! Keep up the fantastic work, and remember to nurture it with love and eco-friendly choices.
                    </MKTypography>
                  </MKBox>
               
                </MKBox>
              </Card>
              <MKBox display="flex" justifyContent="space-between" alignItems="center" mb={1}>
               
              </MKBox>
            </Grid>
          </Grid>
        </Grid>
      </Container>
    </MKBox>
  );
}

export default Tamagotchi;
