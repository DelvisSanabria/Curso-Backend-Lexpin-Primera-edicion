import express from 'express';
import mongoose from 'mongoose';

const app = express();
const MONGO_URI = 'mongodb://mongodb-service:27017/mi_db';
const PORT = 3000;

const visitasSchema = new mongoose.Schema({
  count: { type: Number, default: 0 }
});

const Visitas = mongoose.model('Visitas', visitasSchema);

async function conectarMongo() {
  try {
    await mongoose.connect(MONGO_URI);
    console.log('Conectado a MongoDB');

    let count = await Visitas.findOne();
    if (!count) {
      count = new Visitas({ count: 0 });
      await count.save();
    }
  } catch (error) {
    console.error('Error al conectar a MongoDB:', error);
    setTimeout(conectarMongo, 5000); // Reintentar después de 5 segundos
  }
}

conectarMongo();

app.get('/visitas', async (req, res) => {
  try {
    let count = await Visitas.findOne();
    count.count++;
    await count.save();
    res.send(`<h1>número de visitas: ${count.count}</h1>`);
  } catch (error) {
    console.error('Error al obtener visitas:', error);
    res.status(500).json({ error: 'Error al obtener visitas' });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
});