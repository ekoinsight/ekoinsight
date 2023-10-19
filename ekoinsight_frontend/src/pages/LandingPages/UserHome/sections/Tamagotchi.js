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

import { useState } from "react";

import PropTypes from "prop-types";
import axios from "axios";

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

function Tamagotchi(props) {
  const profile = props.idToken;
  const bearer = props.apiCred;

  console.log("bearer below");
  console.log(bearer);
  const [file, setFile] = useState();

  console.log("profile", profile);

  function handleFileChange(event) {
    setFile(event.target.files[0]);
    console.log("File is ", file);
  }

  function handleSubmit(event) {
    try {
      event.preventDefault();
      const url = `https://api.ekoinsight.ca/user/${profile.sub}/feed`;
      const formData = new FormData();
      console.log(file);
      formData.append("file", file);
      formData.append("fileName", file.name);
      const config = {
        headers: {
          // "Authorization": `Bearer ${bearer}`,
          Authorization: bearer,
          "content-type": "multipart/form-data",
        },
      };
      axios
        .post(url, formData, config)
        .then((response) => {
          console.log(response.data);
        })
        .catch(function (error) {
          window.alert("Your feeding did not succeed :( ! Please try again later.");
          console.log("error below from axios");
          console.log(error.toJSON());
        });
    } catch (error) {
      if (file === undefined) {
        window.alert("Don't forget to upload an image of the item you recycled !");
      } else {
        console.error("Error below");
        console.error(error);
        window.alert("Your feeding did not succeed :( Please try again later.");
      }
    }
  }

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
                      Good morning, Tamagotchi Keeper! Your PlanetPal is thriving today. It woke up
                      with a big smile, well-fed, and full of energy. It&apos;s been living a green
                      and happy life with you! Keep up the fantastic work, and remember to nurture
                      it with love and eco-friendly choices.
                    </MKTypography>
                    <MKBox width="100%" onSubmit={handleSubmit} component="form" autoComplete="off">
                      <MKBox p={3}>
                        <Grid container spacing={3}>
                          <Grid item xs={12}>
                            <MKInput variant="standard" type="file" onChange={handleFileChange} />
                          </Grid>
                        </Grid>
                        <Grid container item justifyContent="center" xs={12} mt={3}>
                          <MKButton type="submit" variant="gradient" color="dark">
                            Feed your PlanetPal !
                          </MKButton>
                        </Grid>
                      </MKBox>
                    </MKBox>
                  </MKBox>
                </MKBox>
              </Card>
              <MKBox
                display="flex"
                justifyContent="space-between"
                alignItems="center"
                mb={1}
              ></MKBox>
            </Grid>
          </Grid>
        </Grid>
      </Container>
    </MKBox>
  );
}

Tamagotchi.propTypes = {
  idToken: PropTypes.object,
  apiCred: PropTypes.string,
};
export default Tamagotchi;