# M5 - Projeto Final Kanvas
API Rest para o gerenciamento de cursos e aulas de uma escola de modalidade EAD.
Utilizei Django Rest Framework para construção da api e suas rotas

### Informações mais detalhadas 
/api/docs/

Rotas: 
| Método HTTP | Caminho | Responsabilidade | Permissão |
|-------------|---------|------------------|-----------|
| POST | /api/accounts/ | Criação de usuário | Livre |
| POST | /api/login/ | Login do usuário | Livre |
| POST | /api/courses/ | Criação de cursos | Somente super usuários |
| GET  | /api/courses/ | Listagem de cursos| Somente usuários autenticados| 
| GET | /api/courses/<course_id>/ | Busca de curso por id |Acesso livre à administradores. Estudantes não podem acessar cursos que não participam| 
| PATCH | /api/courses/<course_id>/ | Atualização somente dos dados de curso | Somente super usuários | 
| DELETE | /api/courses/<course_id>/ | Deleção de curso | Somente super usuários |
| POST | /api/courses/<course_id>/contents/ | Criação de conteúdos e associação ao curso | Somente super usuários |
| GET | /api/courses/<course_id>/contents/<content_id>/ | Busca de conteúdo por id | Super usuários têm acesso livre. Estudantes só podem acessar dos que participam |
| PATCH | /api/courses/<course_id>/contents/<content_id>/ | Atualização somente do conteúdo | Somente super usuários |
| DELETE | /api/courses/<course_id>/contents/<content_id>/ | Deleção de conteúdos | Somente super usuários | 
| PUT | /api/courses/<course_id>/students/ | Adição de alunos ao curso | Somente super usuários |
| GET | /api/courses/<course_id>/students/ | Listagem dos estudantes do curso | Somente super usuários |
| GET | /api/docs/ | Visualização da documentação no formato Swagger ou Redoc | Acesso livre |
