
<body>
  <h1>API Documentation</h1>

  <h2>Endpoints</h2>
  <ul>
    <li><strong>GET /api/add-student/</strong>: Returns a list of all students.</li>
    <li><strong>GET /api/add-student/&lt;int:pk&gt;/</strong>: Returns details of a specific student.</li>
    <li><strong>POST /api/add-student/</strong>: Adds a new student to the database.</li>
    <!-- Add other endpoints here -->
  </ul>

  <h2>Usage</h2>
  <p>To use the API, send HTTP requests to the specified endpoints with the required parameters.</p>
  <h3>Example</h3>

  <h4>Add a new student:</h4>
  <pre>
    <code>
curl -X POST http://yourdomain.com/api/add-student/ -F "first_name=John" -F "last_name=Doe" -F "birthday=2000-01-01" -F "phone_number=123456789" -F "file_name=@/path/to/image.jpg"
    </code>
  </pre>

  <h4>Record a visit day:</h4>
  <pre>
    <code>
curl -X POST http://yourdomain.com/api/visit-student/ -F "file_name=@/path/to/image.jpg"
    </code>
  </pre>

  <!-- Add any additional content here -->

</body>
</html>
