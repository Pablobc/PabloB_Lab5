<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Targets</h1>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Contraseña</th>
              <th scope="col">IP</th>
              <th scope="col">Sistema Operativo</th>
              <th scope="col">Version</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(dato, index) in datos" :key="index">
              <td>{{ dato.id }}</td>
              <td>{{ dato.contrasenia }}</td>
              <td>{{ dato.dip }}</td>
              <td>{{ dato.so }}</td>
              <td>{{ dato.version }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PDFS',
  data() {
    return {
      datos: [],
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/api/grida';
      axios.get(path)
        .then((res) => {
          this.datos = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
