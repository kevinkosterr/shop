import {Box, Card, CardContent, CardMedia, Typography} from "@mui/material";
import {makeStyles} from "@mui/styles";

const useStyles = makeStyles({
    productCard: {
        maxWidth: "350px",
    },
    productPrice: {
        color: "#3f51b5",
        fontWeight: "bold"
    },
    productMedia: {
        display: "block",
        marginLeft: "auto",
        marginRight: "auto",
        maxWidth: "300px"
    }
});

const Product = ({uid, title, price, image}) => {
    const classes = useStyles();

    return (
        <Card className={classes.productCard} variant="outlined">
            <CardMedia
                component="img"
                height={300}
                image={"http://localhost:8000/" + image}
                alt={uid + "_cardImg"}
                className={classes.productMedia}
            />
            <Box className={classes.productCardBox}>
                <CardContent>
                    <Typography variant={"h4"}>
                        {title}
                    </Typography>
                    <Typography variant={"h5"} className={classes.productPrice}>
                        &euro;{price}
                    </Typography>
                </CardContent>
            </Box>
        </Card>
    );
};

export default Product;
