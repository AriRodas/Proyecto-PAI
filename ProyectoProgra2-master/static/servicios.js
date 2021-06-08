let servicios = [
    ['Traslados dentro y fuera de El Salvador', 'Como parte del desarrollo de tu actividad comercial, ya sea para reuniones de negocios, visitas técnicas, envío y entrega de documentos importantes, entre otros.'],
    ['Traslado hasta el aeropuerto', 'Sabemos la importancia de las conexiones, y lo que significa para ti viajar seguro y llegar a tiempo. Desde tu hogar u oficina, desde o hacia el aeropuerto, nos esmeramos en ser confiables y hacer que tu viaje sea confortable.'],
    ['Transporte turístico', 'Disfrutar, tener vivencias únicas y poseer memorias increíbles de nuestro bello país es incomparable. ¡tienes que vivirlo! El Salvador posee una variedad de atractivos turísticos. Conocemos sus ciudades, sus pueblos vivos, su gente y nos encanta acompañarte.'],
    ['Transporte de personal de trabajo', 'Movilizamos a su personal antes o después de su jornada laboral. Lo hacemos con grato placer y le ofrecemos un trato respetuoso y preferencial para cada uno de sus colaboradores. En unidades para 10, 15, 28 o más pasajeros.'],
    ['Transporte para eventos y convenciones', 'Nos volvemos parte de tu marca y nos adaptamos para hacer de tu evento un éxito. Con capacidad y experiencia en logística para movilizar grupos de más de 100 personas.'],
    ['Instituciones educativas', 'Volverte parte de algo siempre tiene un significado especial. Trabajamos con instituciones educativas para llevar a niños, jóvenes, padres de familia y docentes a diferentes actividades de esparcimiento o curriculares. Poseemos excelentes relaciones con escuelas públicas, colegios privados, universidades y centros de enseñanza.'],
];

if(sessionStorage.getItem("servicios")==null){
    sessionStorage.setItem("servicios", JSON.stringify(servicios));
}
