import {React} from 'react'
import {makeStyles} from "@mui/styles";
import {useQuery} from "@apollo/client";

import {getProducts} from "../../graphql/Queries";
import Product from "./Product";
import {Grid} from "@mui/material";
import Container from "@mui/material/Container";

const useStyles = makeStyles({
    productsGrid: {
        width: "100%"
    }
})

export const Products = () => {
    const classes = useStyles();

    const {loading, error, data} = useQuery(getProducts);

    if (loading) return <p>Products are loading...</p>;
    if (error) return <p>Oops.. Something went wrong..</p>;


    return (
        <Container>
            <Grid container className={classes.productsGrid}>
                {data.products.map(({uid, title, image, price}) => (
                    <Grid key={uid} item xs={1} md={3} lg={4}>
                        <Product uid={uid} title={title} image={image} price={price}/>
                    </Grid>
                ))}
            </Grid>
        </Container>
    )
}

