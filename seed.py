from models import User, Post, db
from app import app

# drop and create tables
db.drop_all()
db.create_all()


# deleete old data
User.query.delete()
Post.query.delete()


# sample users
u1 = User(first_name="John", last_name="Johnson")
u2 = User(first_name="George", last_name="Washington")
u3 = User(first_name="Regina", last_name="Spektor")
u4 = User(first_name="Lucy", last_name="DellaVecchia")
u5 = User(first_name="Finn", last_name="Huckleberry")


db.session.add_all([u1, u2, u3, u4, u5])
db.session.commit()

# sample posts
p1 = Post(
    title="Hello",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u1.id,
)
p2 = Post(
    title="I'm a New User!",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u1.id,
)
p3 = Post(
    title="What's New??",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u1.id,
)

p4 = Post(
    title="Hello",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u2.id,
)
p5 = Post(
    title="I'm a New User!",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u3.id,
)
p6 = Post(
    title="What's New??",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u3.id,
)
p7 = Post(
    title="This is how we do it!",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u4.id,
)
p8 = Post(
    title="Blogs are Stupendous",
    content="Lorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae suscipit expedita laborum necessitatibus quos harum praesentium consequuntur ducimus laudantium assumenda, quod debitis iste voluptates dolorem rerum minima reiciendis consectetur? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor maiores, impedit, beatae dolorem est laboriosam labore exercitationem cum reiciendis nostrum assumenda ratione quam, illo quisquam magni laborum fugiat! Praesentium, quam?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae exercitationem quis, labore veniam eligendi delectus excepturi itaque ad illo facere nihil qui molestiae consectetur voluptatem cupiditate earum iure vel reprehenderit. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque nemo nesciunt quibusdam eligendi. Autem quasi, animi unde doloremque aliquid non a ex neque, repellat eaque illum ipsam, velit dolor rem.",
    posted_by=u4.id,
)


db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
db.session.commit()
