import {Card} from "@mui/material";

import {makeStyles} from "@mui/styles";

const useStyles = makeStyles({
    productCard: {
        background: "#E6EBE4"
    }
})

const Product = ({uid, title, price}) => {

    const classes = useStyles();

    return(
        <Card className={classes.productCard}>
        </Card>
    )
}

export default Product;
