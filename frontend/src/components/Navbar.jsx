import AppBar from '@mui/material/AppBar';
import Container from '@mui/material/Container';
import {Typography} from "@mui/material";
import {Toolbar} from "@mui/material";

const Navbar = () => {
    return <div className="navbar">
        <AppBar position="static">
            <Container maxWidth="x1">
                <Toolbar disableGutters>
                    <Typography variant="h6" noWrap component={"div"}>
                        Shop
                    </Typography>
                </Toolbar>
            </Container>
        </AppBar>
    </div>;
};

export default Navbar;
