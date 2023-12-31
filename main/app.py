"""docstring for app"""

from absl import app, flags

FLAGS = flags.FLAGS

flags.DEFINE_bool(name="dry_run", default=False, help="If True don't write metrics")
flags.DEFINE_string(name="name", default="elbowai", help="Name of company")
flags.DEFINE_integer(
    name="num_times", default=2, help="Number of times to print greeting."
)

# Required flag.
flags.mark_flag_as_required(flag_name="dry_run")


def main(argv):
    """main function"""
    if len(argv) < 1:
        raise ValueError("Need more arguments")
    print(FLAGS.dry_run)
    print(FLAGS.num_times)
    for i in range(0, FLAGS.num_times):
        print(i)
    print("-" * 50)
    print(FLAGS.name)


if __name__ == "__main__":
    app.run(main)
