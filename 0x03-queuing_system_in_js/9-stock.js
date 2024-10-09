import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);


const listProducts = [
    {
        itemId: 1,
        itemName: 'Suitcase 250',
        price: 50,
        initialAvailableQuantity: 4,
    },
    {
        itemId: 2,
        itemName: 'Suitcase 450',
        price: 100,
        initialAvailableQuantity: 10,
    },
    {
        itemId: 3,
        itemName: 'Suitcase 650',
        price: 350,
        initialAvailableQuantity: 2,
    },
    {
        itemId: 4,
        itemName: 'Suitcase 1050',
        price: 550,
        initialAvailableQuantity: 5,
    },
]

//setup express server
const app = express();
const port = 1245;

//helper functions
function getItemById(id) {
    return listProducts.find((product) => product.itemId === parseInt(id));
}

async function reserveStockById(itemId, stock) {
    return await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const reservedStock = await getAsync(`item.${itemId}`);
    return reservedStock ? parseInt(reservedStock) : null;
}

// Route to get all available products
app.get('/list_products', (req, res) => {
    res.json(listProducts);
});


// Route to get product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
    const { itemId } = req.params;
    const product = getItemById(itemId);
  
    if (!product) {
      return res.json({ status: 'Product not found' });
    }
  
    const currentStock = await getCurrentReservedStockById(itemId);
    const availableStock = currentStock !== null ? currentStock : product.initialAvailableQuantity;
  
    res.json({
      ...product,
      currentQuantity: availableStock
    });
  });
  
  // Route to reserve product by itemId
  app.get('/reserve_product/:itemId', async (req, res) => {
    const { itemId } = req.params;
    const product = getItemById(itemId);
  
    if (!product) {
      return res.json({ status: 'Product not found' });
    }
  
    const currentStock = await getCurrentReservedStockById(itemId);
    const availableStock = currentStock !== null ? currentStock : product.initialAvailableQuantity;
  
    if (availableStock <= 0) {
      return res.json({
        status: 'Not enough stock available',
        itemId: product.itemId
      });
    }
  
    await reserveStockById(itemId, availableStock - 1);
    res.json({
      status: 'Reservation confirmed',
      itemId: product.itemId
    });
  });
  
app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});