const express = require('express');
const router = express.Router();
const productController = require('../controllers/productController');

// Ruta para obtener conteo de productos (debe ir antes de /products)
router.get('/products/count', productController.getProductsCount);


// Ruta de productos (vulnerable a SQL injection)
router.get('/products', productController.getProducts);

const regex = /;|--/;

const validarSQL = (req, res, next) => {
    const { query } = req.body;

    if (!query || query.trim() === '') {
        return res.status(400).json({ error: "Query vacía no permitida" });
    }

    if (regex.test(query)) {
        return res.status(400).json({ error: "No se permite" });
    }

    next();
};

router.post('/search', validarSQL, (req, res) => {
    const { query } = req.body;

    return res.status(200).json({
        results: [
            { id: 1, name: 'ejemplo', query: query }
        ],
        message: "Búsqueda exitosa"
    });
});

module.exports = router;
