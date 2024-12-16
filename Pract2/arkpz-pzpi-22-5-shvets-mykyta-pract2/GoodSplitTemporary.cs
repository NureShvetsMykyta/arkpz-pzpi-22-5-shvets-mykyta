public abstract class Obstacle : GameElement
{
    public double Speed { get; set; }
    public Direction Direction { get; set; }
    public override bool isKilling { get { return false; } }

    // Інші атрибути та властивості ...

    public void Move()
    {
        lock (field)
        {
            pX = X;

            // Розділення на проміжні змінні
            int newX = X + dx[Direction];
            int widthLimit = field.Width - Length;

            // Обчислення нової позиції
            if (newX % widthLimit == 0)
            {
                X = (Direction == Direction.Left) ? widthLimit - 1 : 1;
            }
            else
            {
                X = newX % widthLimit;
            }

            updateField();
        }
    }

    // Інші методи ...

}

