from absl import app, flags, logging

FLAGS = flags.FLAGS
logging.set_verbosity(logging.INFO)
# Flag names are globally defined!  So in general, we need to be
# careful to pick names that are unlikely to be used by other libraries.
# If there is a conflict, we'll get an error at import time.
flags.DEFINE_string(
    name="name", default="Jane Random", help="Your name.", short_name="n"
)
flags.DEFINE_integer(name="age", default=18, help="Your age in years.", lower_bound=0)
flags.DEFINE_boolean(name="debug", default=False, help="Produces debugging output.")
flags.DEFINE_enum(
    name="job",
    default="running",
    enum_values=["running", "stopped"],
    help="Job status.",
)

flags.DEFINE_integer(name="num_a", default=1, help="Your number a.")
flags.DEFINE_integer(name="num_b", default=1, help="Your number b.")


def add(a: int, b: int) -> int:
    return a + b


def main(argv):
    if FLAGS.debug:
        logging.info(f"non-flag arguments: {argv}")
    logging.info(f"Happy Birthday {FLAGS.name}")
    if FLAGS.age is not None:
        logging.info(f"You are {FLAGS.age} years old, and your job is {FLAGS.job}")
    logging.info(f"Adding two numbers: {add(FLAGS.num_a, FLAGS.num_b)}")


if __name__ == "__main__":
    app.run(main)
