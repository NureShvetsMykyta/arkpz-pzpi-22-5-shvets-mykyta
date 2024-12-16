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
            X = ((X + dx[Direction]) % (field.Width - Length) == 0) 
                ? (Direction == Direction.Left ? field.Width - Length - 1 : 1) 
                : (X + dx[Direction]) % (field.Width - Length);
            updateField();
        }
    }

    // Інші методи ...

}

