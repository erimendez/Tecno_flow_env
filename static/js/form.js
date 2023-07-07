const apiUrl = 'https://sheetdb.io/api/v1/6phulegjdw082';

    // Función para enviar una solicitud POST a la API y crear un registro
    function crearRegistro(event) {
      event.preventDefault();
      console.log('entro')
      const form = document.getElementById('crearForm');
      const formData = new FormData(form);
    
      fetch(apiUrl, {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        // Realizar acciones adicionales después de crear el registro
        console.log('Registro creado:', data);
      })
      .catch(error => {
        console.error('Error al crear el registro:', error);
      });
    }

    // Función para enviar una solicitud GET ala API y obtener los registros existentes

    function obtenerRegistros() {
        fetch(apiUrl)
          .then(response => response.json())
          .then(data => {
            // Mostrar los registros obtenidos en el elemento con id "registros"
            const registrosDiv = document.getElementById('registros');
            registrosDiv.innerHTML = '';
      
            data.forEach(registro => {
              const registroDiv = document.createElement('div');
              registroDiv.innerHTML = `
                <strong>ID:</strong> ${registro.id}<br>
                <strong>Nombre:</strong> ${registro.name}<br>
                <strong>Apellido:</strong> ${registro.lastname}<br>
                <strong>Marca:</strong> ${registro.brand}<br>
                <strong>Estado:</strong> ${registro.status}<br>
                <strong>Capacidad:</strong> ${registro.capacity}<br>
                <strong>Color:</strong> ${registro.colour}<br>
                <strong>Precio sugerido:</strong> ${registro.price}<br>
                <img src="${registro.image}" alt="Imagen del registro"><br><br>
              `;
      
              registrosDiv.appendChild(registroDiv);
            });
          })
          .catch(error => {
            console.error('Error al obtener los registros:', error);
          });
      }

    // Función para enviar una solicitud PUT a la API y actualizar un registro
    function actualizarRegistro(event) {
      event.preventDefault();

      const form = document.getElementById('actualizarForm');
      const formData = new FormData(form);
      const id = formData.get('id');

      fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        // Realizar acciones adicionales después de actualizar el registro
        console.log('Registro actualizado:', data);
      })
      .catch(error => {
        console.error('Error al actualizar el registro:', error);
      });
    }

    // Función para enviar una solicitud DELETE a la API y borrar un registro
    function borrarRegistro(event) {
      event.preventDefault();

      const form = document.getElementById('borrarForm');
      const formData = new FormData(form);
      const id = formData.get('id_borrar');

      fetch(`${apiUrl}/${id}`, {
        method: 'DELETE'
      })
      .then(response => {
        if (response.ok) {
          // Realizar acciones adicionales después de borrar el registro
          console.log('Registro borrado');
        } else {
          throw new Error('Error al borrar el registro');
        }
      })
      .catch(error => {
        console.error('Error al borrar el registro:', error);
      });
    }

    // Agregar los controladores de eventos a los formularios
    document.getElementById('crearForm').addEventListener('submit', crearRegistro);
    document.getElementById('actualizarForm').addEventListener('submit', actualizarRegistro);
    document.getElementById('borrarForm').addEventListener('submit', borrarRegistro);

    // Obtener los registros al cargar la página
    obtenerRegistros();