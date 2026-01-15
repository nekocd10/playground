import express from 'express' ;
import path from 'path' ;

const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');

app.set('views', path.join(process.cwd(), 'views'));

app.use(express.static(path.join(process.cwd(), 'public')));

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('index'); 
});

app.get('/about', (req, res) => {
  res.render('about');
});

app.listen(PORT, () => {
    console.log('i hope this doesnt crash on me')
    });
