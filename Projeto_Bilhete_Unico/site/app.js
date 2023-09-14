const express = require("express");
const cors = require("cors");
const path = require("path");
const port = 8080;

const app = express();

const indexRouter = require("./src/routes/index");
// const registroRouter = require("./src/routes/registros");

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

app.use(cors());

app.use("/", indexRouter);
// app.use("/registros", registroRouter);

app.listen(port, () => {
  console.log("Servidor aberto na porta " + port);
});
